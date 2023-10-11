import React from "react";
import {
  TransformWrapper,
  TransformComponent,
  useControls
} from "react-zoom-pan-pinch";
import Board from "./Board.jsx"

const Game = () => {
  const Controls = () => {
    const { zoomIn, zoomOut, resetTransform } = useControls();
    return (
    <>
        <button onClick={() => zoomIn()}>🔍+</button>
        <button onClick={() => zoomOut()}>🔍-</button>
        <button onClick={() => resetTransform()}>↩️</button>
    </>
    );
  };
  const size = 20;
  const boardState = Array.from({ length: size }, () => Array(size).fill('free'));
  //probando posiciones
  boardState[4][4] = 'tribute';
  boardState[9][17] = 'tribute';
  boardState[19][1] = 'tribute';
  boardState[8][8] = 'item';
  boardState[5][15] = 'item';

  return (
    <main className='board'>
      <h1>The Hunger Games</h1>
      <TransformWrapper>
        <div className= 'button section'><Controls /></div>        
        <TransformComponent>
          <section className='game'>
            <Board size={size} boardState={boardState} />
          </section>
        </TransformComponent>
      </TransformWrapper>
    </main>
  )
}
export default Game