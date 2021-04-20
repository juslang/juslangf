import React, {useEffect} from 'react';
import StockInfo from 'containers/StockInfo';

export default function Index( { test } ) {

  useEffect(() => {
    insKakaoAd();
  }, []);

  const insKakaoAd = () => {
    let ins = document.createElement('ins');
    let scr = document.createElement('script');

    ins.className = 'kakao_ad_area';
    ins.style = "display:none;";
    scr.async = 'true';
    scr.type = "text/javascript";
    scr.src = "//t1.daumcdn.net/kas/static/ba.min.js";
    ins.setAttribute('data-ad-width', '728');
    ins.setAttribute('data-ad-height', '90');
    ins.setAttribute('data-ad-unit', 'DAN-bb1WhMQ0aRuGASM3');
    ins.setAttribute("align", "center");

    document.querySelector('.adfit').appendChild(ins);
    document.querySelector('.adfit').appendChild(scr);
  }
  return (
    <>
        <StockInfo />
        <div className="adfit" />
    </>
  );
}


// export async function getServerSideProps(context) {

//    return { props: { test } };
// }
