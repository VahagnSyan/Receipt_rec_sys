class Detection:
    def __init__(self, data = ''):
        self.data = data

    def detection(self):
        def filter(info) -> list:
            result = []
            index = 2
            while index < len(info):
                # if 'Դաս' in info[index] or 'Դամ' in info[index] or 'Դպա' in info[index]:
                #     result.append(info[index + 1] + '\t\t' + info[index + 2].split(' ')[-1])

                if (
                    "Հատ" in info[index]
                    or "Յ1ատ" in info[index]
                    or "Յատ" in info[index]
                    or "Վատ" in info[index]
                    or "գի" in info[index]
                    or "կգ" in info[index]
                    or "գր" in info[index]
                ):
                    product = dict()
                    product['name'] = find_name(info[index])
                    product['price'] = info[index + 1].split(" ")[-1]
                    product['category'] = ''

                    result.append(product)

                index += 1
            return result

        def result(info):
            text = info.split("\n")
            text2 = [x for x in text if x != ""]
            return filter(text2)

        def find_name(name):
            output_name = ''
            for i in name:
                if i.isdigit():
                    break
                output_name += i
            return output_name

        return result(self.data)