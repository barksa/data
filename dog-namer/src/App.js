import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Header from './Header';
import Main from './Main';
import Result from './Result';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter> 
        <Header />
        <Routes>
          <Route path = '/' element = {<Main />}></Route>
          <Route path = '/result/*' element = {<Result />}></Route>
        </Routes>
      </BrowserRouter>
        {/* <Header />
        <Main />
        <Result /> */}
    </div>
  );
}

export default App;
