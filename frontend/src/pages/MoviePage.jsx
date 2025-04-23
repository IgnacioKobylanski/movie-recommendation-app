import React from 'react';
import { useLocation } from 'react-router-dom';
import '../styles/MoviePage.css';

function MoviePage() {
  const location = useLocation();
  const { name, imageUrl } = location.state || {};

  if (!name || !imageUrl) {
    return <div className="movie-page-error">No movie data available.</div>;
  }

  return (
    <div className="movie-page-container">
      <h1 className="movie-title">{name}</h1>
      <img className="movie-image" src={imageUrl} alt={name} />
      <p className="movie-description">
        Esta es una breve descripción de <strong>{name}</strong>. Pronto vamos a mostrar más info acá.
      </p>
    </div>
  );
}

export default MoviePage;












/* import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function MoviePage() {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5000/movie/${id}`)
      .then((res) => res.json())
      .then((data) => setMovie(data))
      .catch((error) => console.error("Error fetching movie:", error));
  }, [id]);

  if (!movie) return <div>Loading...</div>;

  return (
    <div>
      <h1>{movie.name}</h1>
      <img src={movie.imageUrl} alt={movie.name} />
      <p>{movie.description}</p>
    </div>
  );
}

export default MoviePage; */