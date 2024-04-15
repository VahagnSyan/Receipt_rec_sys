import { FC, useEffect, useState } from "react";
import { IProduct } from "../../types";
import Product from "./Product";

interface IProductsRenderer {
  products: IProduct[];
  isSubmited: boolean;
  editedProducts: any;
  setEditedProducts: any;
  idx: number;
}
const ProductsRenderer: FC<IProductsRenderer> = ({
  products,
  isSubmited,
  editedProducts,
  setEditedProducts,
  idx,
}) => {
  const [currentProducts, setCurrentProducts] = useState(products);

  useEffect(() => {
    let updatedProducts = [...editedProducts];
    updatedProducts[idx].products = currentProducts;
    setEditedProducts(updatedProducts);
  }, [currentProducts]);

  return (
    <>
      {products.map((product, i) => {
        return (
          <Product
            key={i}
            product={product}
            isSubmited={isSubmited}
            editedProducts={currentProducts}
            setEditedProducts={setCurrentProducts}
          />
        );
      })}
    </>
  );
};

export default ProductsRenderer;
