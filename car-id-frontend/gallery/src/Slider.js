import React from "react";
import AwesomeSlider from "react-awesome-slider";
import withAutoplay from "react-awesome-slider/dist/autoplay";
import "react-awesome-slider/dist/styles.css";

function Slider(props) {
  const { images } = props;

  const AutoplaySlider = withAutoplay(AwesomeSlider);

  return (
    <AutoplaySlider
      play={true}
      cancelOnInteraction={false} // should stop playing on user interaction
      interval={15000}>
      {images.map((url, index) => (
        <div key={index} data-src={url} />
      ))}
    </AutoplaySlider>
  );
}

export default Slider;
