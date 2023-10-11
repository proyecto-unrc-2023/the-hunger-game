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
  return (
    <main className='board'>
      <h1>The Hunger Games</h1>
      <TransformWrapper>
        <Controls />
        <TransformComponent>
          <section className='game'>
            <Board/>
          </section>
        </TransformComponent>
      </TransformWrapper>
    </main>
  )
}
export default Game