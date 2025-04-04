import React from 'react';
import '../styles/Header.css';
import logo from '../assets/images/logoW.png';

const Header = () => {
  return (
    <header className="header">
      <div className="logo">
      <img src={logo} alt="MochiMovies Logo" className="logo" />
        
      </div>
      <h1>MochiMovies</h1>
      <nav className='header-nav'>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
