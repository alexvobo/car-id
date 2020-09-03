import React, { useState } from "react";
import Carousel from "react-bootstrap/Carousel";
import Image from "react-bootstrap/Image";
import im from "./test_imgs/lambo.jpg"
function ControlledCarousel(props) {
  const { images } = props;
  return (
    <Carousel indicators={false} className="carousel">
      {images.map((url,index) => (
        
        <Carousel.Item > 
          <Image fluid src={url} alt="" />
        </Carousel.Item>
      ))}
    </Carousel>
  );
}

export default ControlledCarousel;
