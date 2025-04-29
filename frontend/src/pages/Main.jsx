import React, { useState } from 'react';
import "../styles/Main.css"
import MovieCard from '../components/MovieCard';

function Main() {
  const [title, setTitle] = useState('');
  const [recommendations, setRecommendations] = useState([{
    name: "The Shawshank Redemption",
    imageUrl: "https://example.com/shawshank.jpg",
  }]);
  
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
      <h1>Find your new favorite movie!</h1>
      <div className="buttons-main">
      <input
        type="text"
        placeholder="Enter a movie title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={getRecommendations}>Get Recomendations</button>
      </div>
      {error && <p>{error}</p>}
      {recommendations.length > 0 && (
        /*{ <ul>
          {recommendations.map((movie, index) => (
            <MovieCard
              key={index}
              movieInfo={{
                name: movie.name,
                imageUrl: "https://images.pexels.com/photos/33129/popcorn-movie-party-entertainment.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
              }}
            />
          ))}
        </ul> }*/
      )}
    </div>
  );
}

export default Main;
