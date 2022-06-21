from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res_lst = []
        products.sort()
        tmp_res_lst = []
        prefix = ''
        for ch in searchWord:
            new_lst = []
            prefix += ch
            for product in products:
                if product.startswith(prefix):
                    new_lst.append(product)
                    if len(tmp_res_lst) < 3:
                        tmp_res_lst.append(product)
            res_lst.append(tmp_res_lst.copy())
            tmp_res_lst = []
            products = new_lst
        return res_lst


if __name__ == "__main__":
    s = Solution()
    print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'))
    print(s.suggestedProducts(["havana"], 'havana'))
    print(s.suggestedProducts(["bags","baggage","banner","box","cloths"], 'bags'))
