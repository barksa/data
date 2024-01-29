import React from 'react';
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import './Result.css';

function Result(props) {
    return (
        <div>
            <h2>Names</h2>
            <br></br>
            <ul className='nameslist'>
                <li>Name1</li>
                <li>Name2</li>
                <li>Name3</li>
            </ul>
            <Link to = '/'><Button>Go Home</Button></Link>
        </div>
    );
}

export default Result;