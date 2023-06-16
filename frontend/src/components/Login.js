import React from 'react';
import { useNavigate } from 'react-router-dom';
import * as api from '../utils/api';
import styles from '../styles.css';

const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');

    const SetData = async(e) => {
        e.preventDefault();
        const res = await api.login(email,password);
        if (res.status === 200) {
            const data = await res.json();
            localStorage.setItem('user_id', data.id);
            localStorage.setItem('token', data.token);
            console.log(data['token']);
            // refresh page
            window.location.reload(false);

        }
        else if (res.status === 401) {
            alert("Credenciales inválidas");
        }
        else {
            alert("Algo salió mal");
        }
    }

    return (
        <div className="container">
            <div className="row">
                <div className="login col-md-6 offset-md-3 mt-5">
                    <div className="card">
                        <div className="card-header">
                            <h3>Inicia sesión</h3>
                        </div>
                        <div className="card-body">
                            <form className='form-login' onSubmit={SetData}>
                                <div className="form-group">
                                    <label htmlFor="email">Correo electrónico</label>
                                </div>
                                <div className="form-group">
                                    <input type="email" className="form-control" id="email" placeholder="Ingresa tu correo electrónico" value={email} onChange={(e) => setEmail(e.target.value)} required />
                                </div>
                                <div className="form-group">
                                    <label htmlFor="password">Contraseña</label>
                                </div>
                                <div className="form-group">
                                    <input type="password" className="form-control" id="password" placeholder="Ingresa tu contraseña" value={password} onChange={(e) => setPassword(e.target.value)} required />
                                </div>
                                <button type="submit" className="login-btn btn-primary">Iniciar sesión</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Login;

