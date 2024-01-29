import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import ToggleButton from 'react-bootstrap/ToggleButton';
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';
import './Main.css'

const adjectivesList = [
    "calm",
    "energetic",
    "exotic",
    "friendly",
    "cute",
    "charismatic",
    "gentle",
    "playful",
    "clever",
    "faithful"
];

function Main(props) {
    const [values, setValues] = useState({
        img: "",
        breed: "",
        gender: "",
        adjectives: [],
    })

    const handleChange = e => {
        const { name, value, type, checked } = e.target;
        let newValue;

        if (type === 'checkbox') {
            if (checked && values.adjectives.length < 3) {
                newValue = [...values.adjectives, value];
            } else {
                newValue = values.adjectives.filter(item => item !== value);
            }
        } else {
            newValue = value;
        }

        setValues({
            ...values,
            [name]: newValue,
        });
    };

    const handleSubmit = e => {
        e.preventDefault()
        alert(JSON.stringify(values, null, 2))
    }

    return (
        <div className="container">
            <br></br>
            <form onSubmit={handleSubmit}>
                <div>
                    <div className='imginput'>
                        <input type="file" id="photo" name="photo" value={values.img} onChange={handleChange} />
                    </div>
                </div>
                <br></br>
                <div>
                    <label htmlFor="breed">Breed  </label>
                    <input type="text" id="breed" name="breed" value={values.breed} onChange={handleChange} />
                </div>
                <br></br>
                <div>
                    <label>Gender</label><br />
                    <ToggleButtonGroup type="radio" name="gender" >
                        <ToggleButton id="male"
                        name="gender"
                        value="Male"
                        checked={values.gender === 'Male'}
                        onChange={handleChange}>
                            Male
                        </ToggleButton>
                        <ToggleButton id="female"
                        name="gender"
                        value="Female"
                        checked={values.gender === 'Female'}
                        onChange={handleChange}>
                            Female
                        </ToggleButton>
                        <ToggleButton id="idc"
                        name="gender"
                        value="IDC"
                        checked={values.gender === 'IDC'}
                        onChange={handleChange}>
                            IDC
                        </ToggleButton>
                    </ToggleButtonGroup>
                    {/* <label>Gender</label><br />
                    <input
                        type="radio"
                        id="male"
                        name="gender"
                        value="Male"
                        checked={values.gender === 'Male'}
                        onChange={handleChange}
                    />
                    <label htmlFor="male">Male</label><br />
                    <input
                        type="radio"
                        id="female"
                        name="gender"
                        value="Female"
                        checked={values.gender === 'Female'}
                        onChange={handleChange}
                    />
                    <label htmlFor="female">Female</label><br />
                    <input
                        type="radio"
                        id="idc"
                        name="gender"
                        value="IDC"
                        checked={values.gender === 'IDC'}
                        onChange={handleChange}
                    />
                    <label htmlFor="idc">IDC</label><br /> */}
                </div>
                <br></br>
                <p>Name sounds like..</p>
                <br></br>
                <div>
                    <label htmlFor="options">Adjectives (Up to 3):</label><br />
                    {adjectivesList.map((adjective, index) => (
                        <React.Fragment key={index}>
                            <input
                                type="checkbox"
                                id={adjective}
                                name="adjectives"
                                value={adjective}
                                checked={values.adjectives.includes(adjective)}
                                onChange={handleChange}
                                disabled={values.adjectives.length === 3 && !values.adjectives.includes(adjective)}
                            />
                            <label htmlFor={adjective}>{adjective}</label><br />
                        </React.Fragment>
                    ))}
                </div>
                <br></br>
                <Link to='/result'><Button type='submit'>Generate</Button></Link>

            </form>
        </div>
    );
}

export default Main;
