import React, { useState } from 'react';
import "../styles/Main.css"

function Main() {
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
    <div className="main-content">
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

export default Main;
