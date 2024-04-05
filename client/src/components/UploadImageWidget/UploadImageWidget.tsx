import { ChangeEvent, FC, useRef, useState } from "react";
import IMAGES from "../../images/Images";
import { getCurrentUserId } from "../../utils";

interface IUploadImageWidget {
  scanReceipt: (id: string, image: File) => void;
  setIsSubmited: (arg: boolean) => void;
}
const UploadImageWidget: FC<IUploadImageWidget> = ({
  scanReceipt,
  setIsSubmited,
}) => {
  const [dragActive, setDragActive] = useState<boolean>(false);
  const inputRef = useRef<any>(null);
  const [files, setFiles] = useState<any>([]);

  function handleChange(e: ChangeEvent<HTMLInputElement>) {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      for (let i = 0; i < e.target.files["length"]; i++) {
        setFiles((prevState: any) => [...prevState, e.target.files![i]]);
      }
    }
  }

  // function handleSubmitFile(e: ChangeEvent<HTMLInputElement>) {
  //   if (files.length === 0) {
  //     // TODO:  no file has been submitted
  //   } else {
  //     // TODO: write submit logic here
  //   }
  // }

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

  function removeFile(idx: any) {
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
    <div className="w-full bg-transparent rounded-xl">
      <form
        className={`flex justify-center h-full px-[50px] border-[2px] border-dashed border-[#5b6068] rounded-[15px] ${
          dragActive && "bg-[#26262C]"
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
          />vs
          <img
            src={IMAGES.folderIcon}
            alt="folder"
            className="w-[130px] h-[130px"
          />
          <span className="text-center text-white text-[20px] leading-[32px] font-semibold">
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
          <button
            type="button"
            className="bg-[#4352F6] text-white text-[20px] font-semibold py-4 px-8 rounded-xl"
            onClick={() => {
              scanReceipt(getCurrentUserId(), files);
              setIsSubmited(true);
            }}
          >
            Submit
          </button>
          <span className="text-gray-400 text-[14px]">
            Supported Formats - png, jpg
          </span>
          <div className="flex flex-col items-center p-3">
            {files.map((file: any, idx: any) => (
              <div key={idx} className="flex flex-row space-x-5">
                <span className="text-white">{file.name}</span>
                <span
                  className="text-red-500 cursor-pointer"
                  onClick={() => removeFile(idx)}
                >
                  remove
                </span>
              </div>
            ))}
          </div>
        </div>
      </form>
    </div>
  );
};

export default UploadImageWidget;
