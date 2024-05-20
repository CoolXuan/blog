import { FFmpeg } from "@ffmpeg/ffmpeg";
 
const ffmpeg = new FFmpeg();
const changeFormat = async (url) => {
    const response = await fetch(url);
    const blob = await response.blob();
    const name = "1.mp4";
   
    // 加载ffmpeg-core
    if (!isLoadFfmpegCore) {
      messageText.value = "加载ffmpeg-core.js";
      await ffmpeg.load({
        coreURL: "/static/esm/ffmpeg-core.js",
      });
      isLoadFfmpegCore = true;
    }
   // 
    await ffmpeg.writeFile(name, new Uint8Array(await readFromBlobOrFile(blob)));
    await ffmpeg.exec(["-i", name, `${111}.mp4`]);
    isTranscoding = false;
   
    const data = await ffmpeg.readFile(`${111}.mp4`);
    videoSrc.value = URL.createObjectURL(
      new Blob([data.buffer], { type: "video/mp4" })
    );
  };
  const readFromBlobOrFile = (blob) =>
  new Promise((resolve, reject) => {
    const fileReader = new FileReader();
    fileReader.onload = () => {
      resolve(fileReader.result);
    };
    fileReader.onerror = ({
      target: {
        error: { code },
      },
    }) => {
      reject(Error(`File could not be read! Code=${code}`));
    };
    fileReader.readAsArrayBuffer(blob);
  });