import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import * as api from '../utils/api';

const DashboardProyectos = () => {
    const navigate = useNavigate();
    const [proyectos, setProyectos] = useState([]);
    const [tareas, setTareas] = useState([]);
    const [proyecto, setProyecto] = useState({});
    const [tareasProyecto, setTareasProyecto] = useState([]);
    const [tarea, setTarea] = useState({});
    const [showViewModal, setShowViewModal] = useState(false);
    const [showEditModal, setShowEditModal] = useState(false);
    const [showCreateModal, setShowCreateModal] = useState(false);
    const [titulo, setTitulo] = useState('');
    const [descripcion, setDescripcion] = useState('');


    const getProyectos = async () => {
        const res = await api.getProyectos();
        if (res.status === 200) {
            const data = await res.json();
            setProyectos(data);
        }
        else {
            alert("Something went wrong");
        }
    }

    const getTareas = async () => {
        const res = await api.getTareas();
        if (res.status === 200) {
            const data = await res.json();
            setTareas(data);
        }
        else {
            alert("Something went wrong");
        }

    }

    useEffect(() => {
        getProyectos();
        getTareas();
    }, []);




    const openCreateModal = () => {
        setShowCreateModal(true);
    }

    const closeCreateModal = () => {
        setShowCreateModal(false);
        //refresh page
        window.location.reload(false);
    }

    const openViewModal = () => {
        setShowViewModal(true);
    }

    const closeViewModal = () => {
        setShowViewModal(false);
    }

    const openEditModal = (proyecto) => {
        setProyecto(proyecto);
        setTitulo(proyecto.titulo);
        setDescripcion(proyecto.descripcion);
        setShowEditModal(true);
    }

    const closeEditModal = () => {
        setShowEditModal(false);
        window.location.reload(false);
    }

    const Logout = async (e) => {
        e.preventDefault();
        const res = await api.logout();
        if (res.status === 200) {
            localStorage.removeItem('token');
            window.location.reload(false);
        } else {
            alert('Something went wrong');
        }
    }

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = date.getDate();
        const month = date.getMonth() + 1;
        const year = date.getFullYear().toString().slice(-2);
        return `${day}/${month}/${year}`;
    }

    const getStatusLabel = (status) => {
        switch (status) {
            case 1:
                return 'Pendiente';
            case 2:
                return 'En progreso';
            case 3:
                return 'Completada';
            default:
                return '';
        }
    }

    const getProyecto = async (id) => {
        const res = await api.getProyecto(id);
        if (res.status === 200) {
            const data = await res.json();
            setTitulo(data.titulo);
            setDescripcion(data.descripcion);
            return data;
        } else {
            alert('Something went wrong');
        }
    }


    const handleViewClick = (id) => {
        const proyecto = getProyecto(id);
        const tareas = getProyectosTareas(id);
        console.log(tareas);
        setProyecto(proyecto);
        openViewModal();
    }

    const getProyectosTareas = async (id) => {
        const res = await api.getProyectosTareas(id);
        if (res.status === 200) {
            const data = await res.json();
            setTareasProyecto(data);
            return data;
        } else {
            alert('Something went wrong');
        }
    }




    const deleteProyecto = async (id) => {
        const res = await api.deleteProyecto(id);
        if (res.status === 200) {
            window.location.reload(false);
        } else {
            alert('Something went wrong');
        }
    }

    const createProyecto = async (e) => {
        e.preventDefault();
        const res = await api.createProyecto(titulo, descripcion);
        if (res.status === 200) {
            closeCreateModal();
        } else {
            alert('Something went wrong');
        }
    }

    const updateProyecto = async (e) => {
        e.preventDefault();
        const res = await api.updateProyecto(proyecto.id, titulo, descripcion);
        if (res.status === 200) {
            const data = await res.json();
            closeEditModal();
        } else {
            alert('Something went wrong');
        }
    }






    return (
        <div className="container">
            <div className="row">
                <div className="col-md-12">
                    <h1>Proyectos</h1>
                    <button className="add-button btn-primary" onClick={openCreateModal}>Crear</button>
                    <button className="add-button btn-primary" onClick={() => navigate('/')}>Volver a inicio</button>
                    <button className="delete-button btn-danger" onClick={Logout}>Cerrar sesión</button>
                    <table className="registers-table table-bordered">
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Descripción</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {proyectos.map((proyecto) => (
                                <tr key={proyecto.id}>
                                    <td>{proyecto.titulo}</td>
                                    <td>{proyecto.descripcion}</td>
                                    <td>
                                        <button className="add-button btn-primary" onClick={() => handleViewClick(proyecto.id)}>Ver</button>
                                        <button className="edit-button btn-warning" onClick={() => openEditModal(proyecto)}>Editar</button>
                                        <button className="delete-button btn-danger" onClick={() => deleteProyecto(proyecto.id)}>Eliminar</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
            
                </div>
            </div>
            {showViewModal && (
                <div className="modal">
                    <div className="modal-content">
                        <h1>{titulo}</h1>
                        <h2>Descripción</h2>
                        <p>{descripcion}</p>
                        <h2>Tareas</h2>
                        <table className="registers-table table-bordered">
                            <thead>
                                <tr>
                                    <th>Título</th>
                                    <th>Descripción</th>
                                    <th>Fecha de vencimiento</th>
                                    <th>Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                {tareasProyecto.map((tarea) => (
                                    <tr key={tarea.id}>
                                        <td>{tarea.titulo}</td>
                                        <td>{tarea.descripcion}</td>
                                        <td>{formatDate(tarea.fecha_venc)}</td>
                                        <td>{getStatusLabel(tarea.estado_id)}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        <button className="delete-button" onClick={closeViewModal}>Cerrar</button>
                    </div>
                </div>
            )}

            {showEditModal && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={closeEditModal}>&times;</span>
                        <h1>Editar proyecto</h1>
                        <form onSubmit={updateProyecto}>
                            <div className="form-group">
                                    <label htmlFor="titulo">Título</label>
                                    <input type="text" className="form-control" id="titulo" placeholder="Título" defaultValue={proyecto.titulo} onChange={(e) => setTitulo(e.target.value)} />
                                </div>
                                <div className="form-group">
                                    <label htmlFor="descripcion">Descripción</label>
                                    <textarea type="text" className="form-control" id="descripcion" placeholder="Descripción" defaultValue={proyecto.descripcion} onChange={(e) => setDescripcion(e.target.value)} />
                                </div>
                                <button type="submit" className="add-button btn-primary">Editar</button>
                            </form>
                    </div>
                </div>
            )}

            {showCreateModal && (
                <div className="modal">
                    <div className="modal-content">
                        <h1>Crear proyecto</h1>
                        <form onSubmit={createProyecto}>
                                <div className="form-group">
                                <label htmlFor="titulo">Título</label>
                                <input type="text" className="form-control" id="titulo" placeholder="Título" onChange={(e) => setTitulo(e.target.value)} />
                                </div>
                                <div className="form-group">
                                <label htmlFor="descripcion">Descripción</label>
                                <textarea type="text" className="form-control" id="descripcion" placeholder="Descripción" onChange={(e) => setDescripcion(e.target.value)} />
                                </div>
                                <button type="submit" className="add-button btn-primary">Crear</button>
                                <button className="delete-button" onClick={closeCreateModal}>Cerrar</button>
                            </form>
                    </div>
                </div>
            )}

        </div>
    )
}

export default DashboardProyectos;


