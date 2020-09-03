import React, { useState, useEffect } from "react";
import { Container, Spinner, Image } from "react-bootstrap";
import {} from "@tensorflow/tfjs";

function Results(props) {
  const { content } = props;
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // //We will have to figure our resutls out here and update the states, including loading
    if (content) {
      fetch("/api/cars", {
        method: "GET",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
        });
      // const body = new FormData();
      // body.append("upload", content);
      // body.append("regions", "us");
      // fetch("https://api.platerecognizer.com/v1/plate-reader/", {
      //   method: "POST",
      //   headers: {
      //     "Authorization": "Token 8cab4d54103a27051cf45c8db7f808d9565b7f54",
      //   },
      //   body: body,
      // })
      //   .then((res) => res.json())
      //   .then((data) => {
      //     console.log(data);
      //     setLoading(false);
      //   });

      // setLoading(false);

      // Get a reference to the bundled asset and convert it to a tensor
      // const image = { content };
      // const imageAssetPath = Image.resolveAssetSource(image);
      // const response = fetch(imageAssetPath.uri, {}, { isBinary: true });
      // const imageData = response.arrayBuffer();

      // const imageTensor = decodeJpeg(imageData);

      // const prediction = model.classify(imageTensor);
    }
  }, []);

  return (
    <>
      {!loading ? (
        <Container className="results-cont">
          <Image src={content} alt={content} fluid />
          <Container className="results-info"></Container>
        </Container>
      ) : (
        <Spinner className="big-spinner" animation="border" variant="light" />
      )}
    </>
  );
}

export default Results;
