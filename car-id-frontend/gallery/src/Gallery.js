import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import ControlledCarousel from "./ControlledCarousel";
function Gallery(props) {
  const {
    carDB,
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
        <div className="equals">Make</div>
        <select
          placeholder="Select A Brand"
          value={selectedMake}
          onChange={onChangeMake}>
          {listMakes.map((opt) => (
            <option key={opt} value={opt}>
              {opt}
            </option>
          ))}
        </select>
      </Row>
      <Row>
        <div className="equals">Model</div>
        <select
          placeholder="Select A Model"
          value={selectedModel}
          onChange={onChangeModel}>
          {listModels.map((opt) => (
            <option key={opt} value={opt}>
              {opt}
            </option>
          ))}
        </select>
      </Row>
      <Row>
        <div className="equals">Year</div>
        <select
          placeholder="Generations"
          value={selectedYear}
          onChange={onChangeYear}>
          {listYears.map((opt) => (
            <option key={opt} value={opt}>
              {opt}
            </option>
          ))}
        </select>
      </Row>
      <Row>
        <ControlledCarousel images={imageList} />
      </Row>
    </Container>
  );
}

export default Gallery;
