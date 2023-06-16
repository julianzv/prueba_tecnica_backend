import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import * as api from '../utils/api';

const DashboardTareas = () => {
    const navigate = useNavigate();
    const [tareas, setTareas] = useState([]);
    const [titulo, setTitulo] = useState('');
    const [descripcion, setDescripcion] = useState('');
    const [fecha_venc, setFechaVenc] = useState('');
    const [estado_id, setEstadoId] = useState(1);
    const [proyecto_id, setProyectoId] = useState('');
    const [tarea, setTarea] = useState({});
      
    const [showCreateModal, setShowCreateModal] = useState(false)
    const [showUpdateModal, setShowUpdateModal] = useState(false)
    const [proyectos, setProyectos] = useState([]);

    const Logout = async (e) => {
        e.preventDefault();
        const res = await api.logout();
        if (res.status === 200) {
            localStorage.removeItem('token');
            window.location.reload(false);
        } else {
            alert('Error al cargar recursos');
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

    const openCreateModal = () => {
        setShowCreateModal(true);
    }

    const closeCreateModal = () => {
        setShowCreateModal(false);
        //refresh page
        window.location.reload(false);
    }

    const openUpdateModal = (tarea) => {
        setTarea(tarea);
        setTitulo(tarea.titulo);
        setDescripcion(tarea.descripcion);
        setFechaVenc(tarea.fecha_venc);
        setEstadoId(tarea.estado_id);
        setProyectoId(tarea.proyecto_id);

        setShowUpdateModal(true);
    }

    const closeUpdateModal = () => {
        setShowUpdateModal(false);
        //refresh page
        window.location.reload(false);
    }

    const GetTareas = async () => {
        const res = await api.getTareas();
        if (res.status === 200) {
            const data = await res.json();
            setTareas(data);
        } else {
            alert('Error al cargar recursos');
        }
    }

    useEffect(() => {
        GetTareas();
    }, []);

    const GetProyectos = async () => {
        const res = await api.getProyectos();
        console.log(res.status);
        if (res.status === 200) {
            const data = await res.json();
            console.log(data);
            setProyectos(data);
            if (data.length > 0){
                setProyectoId(data[0].id);
            }
        } else {
            alert('Error al cargar recursos');
        }
    }


    useEffect(() => {
        GetProyectos();
    }, []);

    const DeleteTarea = async (id) => {
        const res = await api.deleteTarea(id);
        if (res.status === 200) {
            setTareas(tareas.filter((tarea) => tarea.id !== id));
        } else {
            alert('Error al cargar recursos');
        }
    }

    const UpdateTarea = async (e) => {
        e.preventDefault();
        const res = await api.updateTarea(tarea.id, titulo, descripcion, fecha_venc, estado_id, proyecto_id);
        if (res.status === 200) {
            const data = await res.json();
            setTareas(tareas.map((t) => (t.id === data.id ? data : t)));
            closeUpdateModal();
        } else {
            alert('Error al cargar recursos');
        }
    }

    const UpdateTareaOk = async (id) => {
        const res = await api.updateTareaCompleta(id)
        if (res.status === 200) {
            const data = await res.json();
            setTareas(tareas.map((t) => (t.id === data.id ? data : t)));
            window.location.reload(false);

        } else {
            alert('Error al cargar recursos');
        }

    }




    const CreateTarea = async (e) => {
        e.preventDefault();
        const res = await api.createTarea(titulo, descripcion, fecha_venc, estado_id, proyecto_id);
        if (res.status === 200) {
            const data = await res.json();
            setTareas([...tareas, data]);
            closeCreateModal();
        } else {
            alert('Error al cargar recursos');
        }
    }
      

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-12">
                    <h1>Tareas</h1>
                    <button className="add-button btn-primary" onClick={openCreateModal}>Crear tarea</button>
                    <button className="add-button btn-primary" onClick={() => navigate('/')}>Volver a inicio</button>
                    <button className="delete-button btn-danger" onClick={Logout}>Cerrar sesión</button>
                    <table className="registers-table table-striped">
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Descripción</th>
                                <th>Fecha de vencimiento</th>
                                <th>Proyecto</th>
                                <th>Estado</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {tareas.map((tarea) => (
                                <tr key={tarea.id}>
                                    <td>{tarea.titulo}</td>
                                    <td>{tarea.descripcion}</td>
                                    <td>{formatDate(tarea.fecha_venc)}</td>
                                    <td>{proyectos.find((proyecto) => proyecto.id === tarea.proyecto_id)?.titulo}</td>
                                    <td>{getStatusLabel(tarea.estado_id)}</td>
                                    <td>
                                        <button className="add-button btn-success" onClick={() => UpdateTareaOk(tarea.id)}>Completar</button>
                                        <button className="edit-button btn-warning" onClick={() => openUpdateModal(tarea)}>Editar</button>
                                        <button className="delete-button btn-danger" onClick={() => DeleteTarea(tarea.id)}>Eliminar</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
            {showCreateModal && (
                <div className="modal">
                    <div className="modal-content">
                        <h1>Crear tarea</h1>
                        <form onSubmit={CreateTarea}>
                            <div className="form-group">
                                <label htmlFor="titulo">Título</label>
                                <input type="text" className="form-control" id="titulo" placeholder="Título" onChange={(e) => setTitulo(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="descripcion">Descripción</label>
                                <textarea type="text" className="form-control" id="descripcion" placeholder="Descripción" onChange={(e) => setDescripcion(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="fecha_venc">Fecha de vencimiento</label>
                                <input type="date" className="form-control" id="fecha_venc" placeholder="Fecha de vencimiento" onChange={(e) => setFechaVenc(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="estado_id">Estado</label>
                                <select className="form-control" id="estado_id" onChange={(e) => setEstadoId(e.target.value)}>
                                    <option value="1">Pendiente</option>
                                    <option value="2">En progreso</option>
                                    <option value="3">Completada</option>
                                </select>
                            </div>
                            <select
                                className="form-control"
                                id="proyecto_id"
                                value={proyecto_id || (proyectos.length > 0 ? proyectos[0].id : '')}
                                onChange={(e) => setProyectoId(e.target.value)}
                            >
                                {proyectos.map((proyecto) => (
                                    <option key={proyecto.id} value={proyecto.id}>{proyecto.titulo}</option>
                                ))}
                            </select>

                            <button type="submit" className="add-button btn-primary">Crear</button>
                            <button type="button" className="delete-button btn-danger" onClick={closeCreateModal}>Cancelar</button>
                        </form>
                    </div>
                </div>

            )}
            {showUpdateModal && (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={closeUpdateModal}>&times;</span>
                    <form onSubmit={UpdateTarea}>
                            <div className="form-group">
                                <label htmlFor="titulo">Título</label>
                                <input type="text" className="form-control" id="titulo" placeholder="Título" defaultValue={tarea.titulo} onChange={(e) => setTitulo(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="descripcion">Descripción</label>
                                <textarea type="text" className="form-control" id="descripcion" placeholder="Descripción" defaultValue={tarea.descripcion} onChange={(e) => setDescripcion(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="fecha_venc">Fecha de vencimiento</label>
                                <input type="date" className="form-control" id="fecha_venc" placeholder="Fecha de vencimiento" defaultValue={tarea.fecha_venc} onChange={(e) => setFechaVenc(e.target.value)} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="estado_id">Estado</label>
                                <select className="form-control" id="estado_id" defaultValue={tarea.estado_id} onChange={(e) => setEstadoId(e.target.value)}>
                                    <option value="1">Pendiente</option>
                                    <option value="2">En progreso</option>
                                    <option value="3">Completada</option>
                                </select>
                            </div>
                            <select
                                className="form-control"
                                id="proyecto_id"
                                value={proyecto_id || (proyectos.length > 0 ? proyectos[0].id : '')}
                                onChange={(e) => setProyectoId(e.target.value)}
                            >
                                {proyectos.map((proyecto) => (
                                    <option key={proyecto.id} value={proyecto.id}>{proyecto.titulo}</option>
                                ))}
                            </select>

                            <button type="submit" className="add-button btn-primary">Actualizar</button>
                            <button type="button" className="delete-button btn-danger" onClick={closeUpdateModal}>Cancelar</button>
                        </form>
                    </div>
                </div>

            )}
        </div>
    );
}


export default DashboardTareas;
