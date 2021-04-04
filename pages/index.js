import React from 'react';
import StockInfo from 'containers/StockInfo';

export default function Index( { test } ) {

  return (
    <>
    <h1>Actions!</h1>
    <StockInfo />
    </>
  );
}


// export async function getServerSideProps(context) {

//    return { props: { test } };
// }
