import { ReactBrowser as Router, Routes, Route } from 'react-router-dom'


import Main from './Main'


function ReactRouter() {

    return (
        <Router>
            <Routes>
                <Route exact path='' element={<Main />}/>
            <Routes/>
        <Router/>
    )
}