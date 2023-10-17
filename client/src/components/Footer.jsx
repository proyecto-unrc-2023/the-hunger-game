import React from 'react';
import './Footer.css'; // Asegúrate de que la ruta del archivo CSS sea correcta

export default function Footer() {
    return (
        <div className='footer'>
            <div className='text-center p-3 center-content'>
                <section className="game-title">
                    <div className="top">    Te gustaria unirte? </div>
                    <div className="bottom" aria-hidden="true">Te gustaria unirte? </div>
                </section>
                <button className="cssbuttons-io-button">
                    Register!
                    <div className="icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                            <path fill="none" d="M0 0h24v24H0z"></path><path fill="currentColor" d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"></path>
                        </svg>
                    </div>
                </button>
            </div>

        </div>
    );
}
