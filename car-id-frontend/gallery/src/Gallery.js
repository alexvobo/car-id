import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Slider from "./Slider";

function Gallery(props) {
  const {
    listMakes,
    selectedMake,
    listModels,
    selectedModel,
    listYears,
    selectedYear,
    onChangeMake,
    onChangeModel,
    onChangeYear,
    imageList,
  } = props;

  return (
    <Container fluid>
      <Row className="selectBoxes">
        <Col>
          <div className="equals">Make</div>
          <select
            placeholder="Select A Brand"
            value={selectedMake}
            onChange={onChangeMake}>
            {listMakes.map((opt, index) => (
              <option key={index} value={opt}>
                {opt}
              </option>
            ))}
          </select>
        </Col>
        <Col>
          <div className="equals">Model</div>
          <select
            placeholder="Select A Model"
            value={selectedModel}
            onChange={onChangeModel}>
            {listModels.map((opt, index) => (
              <option key={index} value={opt}>
                {opt}
              </option>
            ))}
          </select>
        </Col>
        <Col>
          <div className="equals">Year</div>
          <select
            placeholder="Generations"
            value={selectedYear}
            onChange={onChangeYear}>
            {listYears.map((opt, index) => (
              <option key={index} value={opt}>
                {opt}
              </option>
            ))}
          </select>
        </Col>
      </Row>
      <Row className="imgGallery">
        <Container fluid>
          <Slider images={imageList} />
        </Container>
      </Row>
      {/* <Row>
        <div className="footer">
          <h4>
            Images provided by
            <a href="https://autoevolution.com" target="_blank">
              Auto Evolution
            </a>
          </h4>
          <h4>
            <a
              href="http://moonlandingsol.pythonanywhere.com/"
              target="_blank">API</a>
          </h4>
        </div>
      </Row> */}
    </Container>
  );
}

export default Gallery;
