import React from 'react';
import { useLocation } from 'react-router-dom';
import "../styles/MoviePage.css"

function MoviePage() {
  const location = useLocation();
  const movie = location.state?.movieInfo;

  if (!movie) {
    return <p>Error: no data founded</p>;
  }
  console.log(movie); 

  return (
    <div className='movie-page-container'>
      <h1>{movie.name}</h1>
      <img src={movie.imageUrl} alt={movie.name} />
      <p className="movie-description">{movie.description}</p>
    </div>
  );
}

export default MoviePage;
