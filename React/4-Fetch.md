// for redirecting 
import { useNavigate } from 'react-router-dom'
const navigate = useNavigate()
navigate('/') //=> homepage

// window.location.reload()



// FETCH DATA:

import { useState, useEffect } from 'react'


const [ articles, setArticles ] = useState([])

// FIRST METHOD:
    const getData = async() => {
        const response = await fetch('http://127.0.0.1:8000/', {
            'method': 'GET',
            headers:  {
                'content-type':'application/json',
                'Authorization':'Token dacb66582e0326ca4ec42cfe31938aef3542705c'
            },
        });
        const jsonData = await response.json()
        setArticles(jsonData)
    }

    useEffect(()=> {
        getData()
    }, [])


// SECOND METHOD:
    useEffect(() => {
        fetch('http://127.0.0.1:8000/', {
            'method': 'GET',
            headers:  {
                'content-type':'application/json',
                'Authorization':'Token dacb66582e0326ca4ec42cfe31938aef3542705c'
            },
        })
        .then((resp)=>resp.json())
        .then((resp)=>setArticles(resp))
        .catch((error)=>console.log(error))
    }, [])