import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import DashboardUsuariosTareas from "./components/DashboardUsuariosTareas";
import Home from "./components/Home";
import DashboardTareas from "./components/DashboardTareas";

function App() {
  const isLoggedIn = localStorage.getItem('token') !== null;
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={isLoggedIn ? <Home/> : <Login />} />
      <Route path="/usuarios-tareas" element={isLoggedIn ? <DashboardUsuariosTareas/> : <Login />} />
      <Route path="/tareas" element={isLoggedIn ? <DashboardTareas/> : <Login />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;
