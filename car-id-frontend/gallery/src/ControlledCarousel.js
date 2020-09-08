import React, { useState } from "react";
import Carousel from "react-bootstrap/Carousel";
import Image from "react-bootstrap/Image";

function ControlledCarousel(props) {
  const { images } = props;

  return (
    <Carousel indicators={true} className="carousel">
      {images.map((url, index) => (
        <Carousel.Item key={index}>
          <Image fluid src={url} alt={index} />
        </Carousel.Item>
      ))}
    </Carousel>
  );
}

export default ControlledCarousel;
