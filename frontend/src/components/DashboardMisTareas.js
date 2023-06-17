/*
DashboardMisTareas: 
Componente que muestra el listado de las tareas asignadas al usuario logueado.
Accesible desde la vista de Home.
*/


import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import * as api from '../utils/api';

const DashboardMisTareas = () => {
    const navigate = useNavigate();
    const user_id = localStorage.getItem('user_id');
    const [tareas, setTareas] = useState([]);
    const [proyectos, setProyectos] = useState([]);
    const [email, setEmail] = useState('');

    useEffect(() => {
        const fetchTareas = async () => {
            const res = await api.getTareasUsuarioAsignadas(user_id);
            if (res.status === 200) {
                const data = await res.json();
                setTareas(data);
            }
            else {
                alert("Error al cargar recursos");
            }
        }
        fetchTareas();
    }

        , [user_id]);

    useEffect(() => {
        const fetchProyectos = async () => {
            const res = await api.getProyectos();
            if (res.status === 200) {
                const data = await res.json();
                setProyectos(data);
            }
            else {
                alert("Error al cargar recursos");
            }
        }
        fetchProyectos();
    }

        , []);

    useEffect(() => {
        const fetchUser = async () => {
            const res = await api.getUsuario(user_id);
            if (res.status === 200) {
                const data = await res.json();
                setEmail(data.correo);
            }
            else {
                alert("Error al cargar recursos");
            }
        }
        fetchUser();
    }

        , [user_id]);


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
        const day = date.getDate() + 1;
        const month = date.getMonth() + 1;
        const year = date.getFullYear().toString().slice(-2);
        return `${day}/${month}/${year}`;
        };
    
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
        };
    

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-12">
                    <h1>Mis Tareas</h1>
                    <h3>Hola, {email}</h3>
                    <h3>Estas son tus tareas pendientes.</h3>
                    <button className="add-button btn-primary" onClick={() => navigate('/')}>Volver a inicio</button>
                    <button className="delete-button btn-primary" onClick={Logout}>Cerrar sesión</button>
                    <table className="registers-table table-striped">
                        <thead>
                            <tr>
                                <th scope="col">Tarea</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Fecha de vencimiento</th>
                                <th scope="col">Estado</th>
                                <th scope="col">Proyecto</th>
                                </tr>
                        </thead>
                        <tbody>
                            {tareas.map((tarea) => (
                                <tr key={tarea.id}>
                                    <td>{tarea.tarea.titulo}</td>
                                    <td>{tarea.tarea.descripcion}</td>
                                    <td>{formatDate(tarea.tarea.fecha_venc)}</td>
                                    <td>{getStatusLabel(tarea.tarea.estado_id)}</td>
                                    <td>{proyectos.find((proyecto) => proyecto.id === tarea.tarea.proyecto_id)?.titulo}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default DashboardMisTareas;




