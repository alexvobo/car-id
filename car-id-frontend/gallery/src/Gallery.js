import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import ControlledCarousel from "./ControlledCarousel";
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
      <Row>
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
            {listYears.map((opt,index) => (
              <option key={index} value={opt}>
                {opt}
              </option>
            ))}
          </select>
        </Col>
      </Row>
      <Row>
        <Container className="image">
          <ControlledCarousel images={imageList} />
        </Container>
      </Row>
    </Container>
  );
}

export default Gallery;
