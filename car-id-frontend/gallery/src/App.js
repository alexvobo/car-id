import React, { useState, useEffect } from "react";
import Gallery from "./Gallery";
import "./App.css";


const BASE_URL = "http://127.0.0.1:5000/";

function prep_for_api(string) {
  return string.replace(" ", "-").replace("class", "klasse").toLowerCase();
}
function App() {
  const [listMakes, setListMakes] = useState([]);
  const [listModels, setListModels] = useState([]);
  const [listYears, setListYears] = useState([]);
  const [make, setMake] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [imageList, setimageList] = useState([]);
  useEffect(() => {
    // Get Makes
    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        setListMakes(data);
        setMake("Lamborghini");
      });
  }, []);
  useEffect(() => {
    // Get Models
    // Hacky solution to call API
    var fetchMake = prep_for_api(make);
    if (fetchMake) {
      fetch(BASE_URL + fetchMake)
        .then((res) => res.json())
        .then((data) => {
          setListModels(data);
          setModel("Murcielago");
        });
    }
  }, [make]);
  useEffect(() => {
    var fetchMake = prep_for_api(make);
    var fetchModel = prep_for_api(model);
    if (fetchMake && fetchModel) {
      fetch(BASE_URL + fetchMake + "/" + fetchModel + "/years")
        .then((res) => res.json())
        .then((data) => {
          setListYears(data);
          setYear(data[0]);
        });
    }
  }, [model]);
  useEffect(() => {
    var fetchMake = prep_for_api(make);
    var fetchModel = prep_for_api(model);
    fetch(BASE_URL + fetchMake + "/" + fetchModel + "/" + year)
      .then((res) => res.json())
      .then((data) => {
        if (fetchModel) {
          var imageUrls = data[fetchModel]["images"].slice(0,2);
          console.log(imageUrls);
          //setimageList(["../test_imgs/lambo.jpg"]);
          setimageList(imageUrls)
        }
      });
  }, [year]);
  return (
    <div id="main" className="main-container">
      <h1>Find Car</h1>

      <Gallery
        onChangeMake={(e) => setMake(e.target.value)}
        onChangeModel={(e) => setModel(e.target.value)}
        onChangeYear={(e) => setYear(e.target.value)}
        selectedMake={make}
        selectedModel={model}
        slectedYear={year}
        listMakes={listMakes}
        listModels={listModels}
        listYears={listYears}
        imageList={imageList} 
      />
  
    </div>
  );
}

export default App;
