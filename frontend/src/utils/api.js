import React, { Component } from 'react';

const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'x-auth-token': localStorage.getItem('token')
}

export function login(email,password) {
    return fetch('http://localhost:8080/api/login', {
        method: 'POST',
        headers: headers,
        body: JSON.stringify({email, password})
    })
    .then(res => res.json())
    .then(data => data)
    .catch(err => console.log(err))
}

export function logout(){
    return fetch('http://localhost:8080/api/logout', {
        method: 'POST',
        headers: headers
    })
}