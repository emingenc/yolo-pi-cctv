import { StatusBar } from 'expo-status-bar';
import React, {useEffect, useState} from 'react';
import { StyleSheet, Text, View } from 'react-native';
import axios from 'axios';


export default function App() {

  const [images,setImages]=useState([]);

  useEffect(() => {
    axios.get(`http://192.168.88.132:8000/latest`)
      .then(res => {
        const images = res.data;
        console.log(images)
        setImages(images);
      })
  }, []);

  return (
    <View style={styles.container}>
      <Text>pi-cctv app</Text>
      {images.map(image => {
        return(
          <div key={image.time}>
            <h4>{image.image_name}  frame: {image.frame}</h4>
            <h4>device name: {image.device_name}</h4>
            <h4>time: {image.time}</h4>
            <p>
            <img src={`data:image/jpeg;base64,${image.image}`} style={{width:"700px"}}/>
            </p>
          </div>
        )
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
