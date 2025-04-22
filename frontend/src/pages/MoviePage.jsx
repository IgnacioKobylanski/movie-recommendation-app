import React, { useEffect, useState } from 'react';
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

export default MoviePage;