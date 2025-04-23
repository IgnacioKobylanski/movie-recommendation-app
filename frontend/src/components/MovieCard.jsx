import React from "react";
import "../styles/MovieCard.css";
import { Link } from "react-router-dom";

const MovieCard = ({ movieInfo }) => {
    const movieId = movieInfo.name.replace(/\s+/g, '-').toLowerCase();

    return (
        <Link
            to={`/movie/${movieId}`}
            className="movie-card-link"
            state={{ name: movieInfo.name, imageUrl: movieInfo.imageUrl }}
        >
            <div className="movie-card-container">
                <img
                    className="movie-small-image"
                    src={movieInfo.imageUrl}
                    alt={movieInfo.name}
                />
                <h3>{movieInfo.name}</h3>
            </div>
        </Link>
    );
};

export default MovieCard;




/* import React from "react";
import "../styles/MovieCard.css"
import { Link } from "react-router-dom";

const MovieCard = ({ movieInfo }) => {
    const movieId = movieInfo.name.replace(/\s+/g, '-').toLowerCase();
    return (
        <Link to={`/movie/${movieId}`} className="movie-card-link">
        <div className="movie-card-container">
            <img
                className="movie-small-image"
                src={movieInfo.imageUrl}
                alt={movieInfo.name}
            />
            <h3>{movieInfo.name}</h3>
        </div>
        </Link>
    );
};

export default MovieCard; */