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
        This is a description of <strong>{name}</strong>. We'll include more info soon!.
      </p>
    </div>
  );
}

export default MoviePage;