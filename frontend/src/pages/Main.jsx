import React, { useState } from 'react';
import "../styles/Main.css";
import MovieCard from '../components/MovieCard';
import { useNavigate } from 'react-router-dom';

function Main() {
  const [title, setTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const getRecommendations = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/recommendations?title=${title}`);
      const data = await response.json();

      if (data.error) {
        setError(data.error);
        setRecommendations([]);
      } else {
        console.log("Recomendaciones del backend:", data.recommendations);
        setRecommendations(data.recommendations);
        setError('');
      }
    } catch (err) {
      console.error(err);
      setError('Hubo un error al obtener las recomendaciones.');
    }
  };

  const handleCardClick = (movie) => {
    navigate(`/movie/${movie.name}`, { state: { movieInfo: movie } });
  };

  return (
    <div className="main-content">
      <h1>Find your new favorite movie!</h1>
      <div className="buttons-main">
        <input
          type="text"
          placeholder="Enter a movie title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button onClick={getRecommendations}>Get Recommendations</button>
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="movie-card-list">
        {recommendations.map((movie, index) => (
          <div key={index} onClick={() => handleCardClick(movie)} style={{ cursor: 'pointer' }}>
            <MovieCard
              movieInfo={{
                name: movie.name,
                imageUrl: movie.imageUrl,
                description: movie.description,
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Main;