import React, { useState, useEffect } from "react";
import "./App.css";
import "./Filedrop.js";
import Filedrop from "./Filedrop.js";
import Results from "./Results.js";

function App() {
  // Upon dropping an image, it will update our image state.
  // Upon passing the file, we will display the results
  // Figure out a way to reset the prompt

  return (
    <>
      <Filedrop />
    </>
  );
}

export default App;
