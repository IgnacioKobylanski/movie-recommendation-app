import React from "react";
import "../styles/MovieCard.css"

const MovieCard = ({ movieInfo }) => {
    return (
        <div className="movie-card-container">
            <img
                className="movie-small-image"
                src={movieInfo.imageUrl}
                alt={movieInfo.name}
            />
            <h3>{movieInfo.name}</h3>
            

        </div>
    );
};

export default MovieCard;