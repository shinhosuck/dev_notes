<!-- AXIOS.JS -->
import axios from 'axios'

const baseUrl = 'http://127.0.0.1:8000/api/'

export const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('access_token')
            ? 'Bearer ' + localStorage.getItem('access_token')
            : null,
        'Content-Type': 'application/json',
        accept: 'application/json'
    },
});


<!-- FROMS.JS -->
import { Link, useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { axiosInstance } from './Axios'

<!-- Register Form -->
export const RegisterForm = () => {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassWord] = useState('')

    const nav = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        setUsername('')
        setEmail('')
        setPassWord('')

        axiosInstance.post('user/register/', {
            'username': username,
            'email': email,
            'password': password
        })
        .then((resp) =>{
            nav('/login');
            console.log(resp)
            console.log(resp.data)
        })
        .catch((error)=> {
            console.log(error)
        })
    };
    
    useEffect(() => {
    }, [])

    return (
        <div className="form-container">
            <div className="form" onSubmit={handleSubmit}>
                <form id='register-form'>
                    <h2>Register Form</h2>
                    <label htmlFor="username">Username</label>
                    <input type="text" id='username' name='username'
                        value={username}
                        onChange={(e)=>setUsername(e.target.value.replaceAll(' ',''))}
                    />
                    <label htmlFor="email">Email</label>
                    <input type="email" id='email' name='email'
                        value={email}
                        onChange={(e)=>setEmail(e.target.value)}
                    />
                    <label htmlFor="password">Password</label>
                    <input type="password" id='password' name='password'
                        value={password}
                        onChange={(e)=>setPassWord(e.target.value)}
                    />
                    <button type="submit">Register</button>
                </form>
                <div className='have-account'>
                    {/* <Link to='/login'>Forgot password?</Link> */}
                    <Link to='/login'>Already have an account? Login</Link>
                </div>
            </div>
        </div>
    )
}

<!-- Login Form -->
export const LoginForm = () => {
    const [username, setUsername] = useState('')
    const [password, setPassWord] = useState('')


    const nav = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        setUsername('')
        setPassWord('')

        axiosInstance.post('token/', {
            'username': username,
            'password': password
        })
        .then((resp) =>{
            localStorage.setItem('access_token', resp.data.access);
            localStorage.setItem('access_token', resp.data.refresh);
            axiosInstance.defaults.headers['Authorization'] = 
            'JWT ' + localStorage.getItem('access_token')
            nav('/');
            console.log(resp.data)
        })
        .catch((error)=> {
            console.log(error)
        })
    };
    
    return (
        <div className="form-container">
            <div className="form">
                <form id="login-form" onSubmit={handleSubmit}>
                    <h2>Login Form</h2>
                    <label htmlFor="username">Username</label>
                    <input type="text" id='username' name='username'
                          value={username}
                          onChange={(e)=>setUsername(e.target.value.replaceAll(' ',''))}
                    />
                    <label htmlFor="password">Username</label>
                    <input type="password" id='password' name='password'
                        value={password}
                        onChange={(e)=>setPassWord(e.target.value)}
                    />
                    <button type='submit'>Login</button>
                </form>
                <div className='forgot-password'>
                    <Link to='/login'>Forgot password?</Link>
                    {/* <Link to='/login'>Already have an account? Login</Link> */}
                </div>
            </div>
        </div>
    )
}