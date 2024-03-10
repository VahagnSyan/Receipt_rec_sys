import { ChangeEvent, useRef, useState } from "react";
import IMAGES from "../../images/Images";

const UploadImageWidget = () => {
  const [dragActive, setDragActive] = useState<boolean>(false);
  const inputRef = useRef<any>(null);
  const [files, setFiles] = useState<any>([]);

  function handleChange(e: ChangeEvent<HTMLInputElement>) {
    e.preventDefault();
    console.log("File has been added");
    if (e.target.files && e.target.files[0]) {
      console.log(e.target.files);
      for (let i = 0; i < e.target.files["length"]; i++) {
        setFiles((prevState: any) => [...prevState, e.target.files![i]]);
      }
    }
  }

  function handleSubmitFile(e: ChangeEvent<HTMLInputElement>) {
    if (files.length === 0) {
      // TODO:  no file has been submitted
    } else {
      // TODO: write submit logic here
    }
  }

  function handleDrop(e: any) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      for (let i = 0; i < e.dataTransfer.files["length"]; i++) {
        setFiles((prevState: any) => [...prevState, e.dataTransfer.files[i]]);
      }
    }
  }

  function handleDragLeave(e: any) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
  }

  function handleDragOver(e: any) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(true);
  }

  function handleDragEnter(e: any) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(true);
  }

  function removeFile(fileName: any, idx: any) {
    const newArr = [...files];
    newArr.splice(idx, 1);
    setFiles([]);
    setFiles(newArr);
  }

  function openFileExplorer() {
    inputRef.current.value = "";
    inputRef.current.click();
  }

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white p-[30px] rounded-[20px]">
        <form
          className={`flex justify-center bg-[#F3F6FD] px-[50px] border-[2px] border-dashed border-[#C7CDD8] rounded-[15px] ${
            dragActive && "bg-[#d7e2fa]"
          }`}
          onDragEnter={handleDragEnter}
          onSubmit={(e) => e.preventDefault()}
          onDrop={handleDrop}
          onDragLeave={handleDragLeave}
          onDragOver={handleDragOver}
        >
          <div className="w-[70%] flex flex-col items-center justify-center gap-[10px]">
            <input
              placeholder="fileInput"
              className="hidden"
              ref={inputRef}
              type="file"
              multiple={true}
              onChange={handleChange}
              accept=".jpeg,.jpg,.png,.heic"
            />
            <img
              src={IMAGES.folderIcon}
              alt="folder"
              className="w-[130px] h-[130px]"
            />
            <span className="text-center text-[#535B6F] text-[20px] leading-[32px] font-semibold">
              Drag your receipts images here to start detection.
            </span>
            <div className="w-[50%] flex items-center justify-between gap-[10px]">
              <hr className="w-full h-[3px] bg-[#8D9EB9]" />
              <span className="text-[#8E9EB5] text-[20px] font-medium">OR</span>
              <hr className="w-full h-[3px] bg-[#8D9EB9]" />
            </div>
            <button
              className="bg-[#4352F6] text-white text-[20px] font-semibold py-4 px-8 rounded-xl"
              onClick={openFileExplorer}
            >
              Browse Files
            </button>
            <span className="text-gray-400 text-[14px]">
              Supported Formats - png, jpg, gif, heic
            </span>
            <div className="flex flex-col items-center p-3">
              {files.map((file: any, idx: any) => (
                <div key={idx} className="flex flex-row space-x-5">
                  <span>{file.name}</span>
                  <span
                    className="text-red-500 cursor-pointer"
                    onClick={() => removeFile(file.name, idx)}
                  >
                    remove
                  </span>
                </div>
              ))}
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default UploadImageWidget;
