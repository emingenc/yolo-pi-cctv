import Carousel, { Dots } from '@brainhubeu/react-carousel';
import '@brainhubeu/react-carousel/lib/style.css'; import { useState } from 'react';

const App = () => {
  const [value, setValue] = useState(0);

  const onChange = value => {
  setValue(value);
  }
  
  //fake api call
  const images = ['https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg',
                  'https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072821__340.jpg',
                  'https://cdn.pixabay.com/photo/2017/12/10/20/56/feather-3010848__340.jpg',
                  'https://cdn.pixabay.com/photo/2015/10/12/14/59/milky-way-984050__340.jpg',
                  'https://cdn.pixabay.com/photo/2017/04/09/09/56/avenue-2215317__340.jpg',
                  'https://cdn.pixabay.com/photo/2017/05/09/03/46/alberta-2297204__340.jpg',
                  'https://cdn.pixabay.com/photo/2020/02/15/16/09/loveourplanet-4851331__340.jpg',
                  'https://cdn.pixabay.com/photo/2013/10/09/02/27/lake-192990__340.jpg',
                  'https://cdn.pixabay.com/photo/2014/02/27/16/08/splashing-275950__340.jpg',
                  'https://cdn.pixabay.com/photo/2018/05/30/15/39/thunderstorm-3441687__340.jpg', ]

  return (
    <div>
      <Carousel
        value={value}
        onChange={onChange}
      >
        {images.map(image=>{
          return <img key={images.indexOf(image)} style={{width:'1080px'}} className="img-example" src={image} />
        })}
      </Carousel>
      <Dots
        value={value}
        onChange={onChange}
        thumbnails={ 
          images.map( image => {
            return (<img key={images.indexOf(image)} style={{width:'128px'}} src={image} />)
            })
         }
      />
    </div>
  );
};

export default App;
