import React, { useCallback, useState, useEffect } from "react";
import { useDropzone } from "react-dropzone";
import { Container, Row, Col, Alert } from "react-bootstrap";
import { Download } from "react-bootstrap-icons";
import Results from "./Results.js";

function Filedrop() {
  //image/file states and validators
  const [image, setImage] = useState();
  const [invalidFile, setinvalidFile] = useState();
  const validFileExtensions = ["PNG", "JPG", "JPEG"];
  function validExt(fname) {
    return validFileExtensions.includes(
      fname.slice(fname.length - 3).toUpperCase()
    );
  }
  //manage clipboard

  //manage dropzone
  const onDrop = useCallback((acceptedFiles) => {
    const mainFile = acceptedFiles[0];
    // Check if File Valid
    if (validExt(mainFile.path)) {
      // File is Valid, set image state
      setinvalidFile(false);
      setImage(URL.createObjectURL(mainFile));
    } else {
      //File is Invalid
      setinvalidFile(true);
    }
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  //Handler and Listener for pasting image
  const pasteImage = useCallback((event) => {
    if (event.keyCode === 70) {
      //F is pressed,
      console.log(window.clipboardData);

      // if (validExt(mainFile)) {
      //   // File is Valid, set image state
      //   setinvalidFile(false);
      //   setImage(URL.createObjectURL(mainFile));
      // } else {
      //   //File is Invalid
      //   setinvalidFile(true);
      // }
    }
  }, []);
  useEffect(() => {
    if (!image) {
      //document.addEventListener("keydown", pasteImage, false);
      document.addEventListener("paste", (e) => {
        let mainFile = e.clipboardData.items[1].getAsFile();
        if (mainFile) {
          console.log(mainFile);
          console.log(mainFile.name);
          if (validExt(mainFile.name)) {
            // File is Valid, set image state
            setinvalidFile(false);
            setImage(URL.createObjectURL(mainFile));
          } else {
            //File is Invalid
            setinvalidFile(true);
          }
        }
      });

      // return () => {
      //   document.removeEventListener("keydown", pasteImage, false);
      // };
    }
  }, []);

  return (
    <>
      {!image ? (
        <Container className="drop-card">
          <Container className="drop-outline" {...getRootProps()}>
            {invalidFile ? (
              <Alert variant="danger">
                Invalid File. Valid Formats:{" "}
                {validFileExtensions.toString().split(",").join(", ")}
              </Alert>
            ) : null}
            <Row>
              <Col>
                <Download size={77} />
              </Col>
            </Row>
            <Row>
              <Col>
                <input {...getInputProps()} />
                {isDragActive ? (
                  <p className="drop-zone-text">
                    Drop the file in this zone ...
                  </p>
                ) : (
                  <p className="drop-zone-text">
                    Drag 'n' drop or click to select a file
                  </p>
                )}
              </Col>
            </Row>
            <Row>
              <Col className="instructions">
                <small>Shortcuts</small>
                <small>CTRL+C: Copy</small>
                <small>CTRL+V: Paste</small>
              </Col>
            </Row>
          </Container>
        </Container>
      ) : (
        <Results content={image} />
      )}
    </>
  );
}

export default Filedrop;
