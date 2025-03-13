import React, { useState } from 'react';

function App() {
  const [title, setTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState('');

  const getRecommendations = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/recommendations?title=${title}`);
      const data = await response.json();
      if (data.error) {
        setError(data.error);
        setRecommendations([]);
      } else {
        setRecommendations(data.recommendations);
        setError('');
      }
    } catch (err) {
      setError('Hubo un error al obtener las recomendaciones.');
    }
  };

  return (
    <div className="App">
      <h1>Recomendaciones de Películas</h1>
      <input
        type="text"
        placeholder="Ingresa un título de película"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={getRecommendations}>Obtener Recomendaciones</button>
      {error && <p>{error}</p>}
      {recommendations.length > 0 && (
        <ul>
          {recommendations.map((movie, index) => (
            <li key={index}>{movie}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;



/* import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
 */