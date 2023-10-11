// Board.js
import React from "react";
import "./Board.css";
import { Square } from './Square.jsx'

const Board = () => {
  // const board = Array(9).fill(null)
  // board.map((square, index) => {
  //   return (
  //     <Square
  //       key={index}
  //       index={index}
  //       // updateBoard={updateBoard}
  //     >
  //       {square}
  //     </Square>
  //   )
  // })
  return (
  <div>acá el tablero
  <img
    src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    alt="test"
    width="100%"
  />
  </div>
  )
}
export default Board;
