def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human = convert_age(cat_age,
                            first_block=15,
                            second_block=9,
                            block_size=4
                            )
    dog_human = convert_age(dog_age,
                            first_block=15,
                            second_block=9,
                            block_size=5
                            )
    return [cat_human, dog_human]


def convert_age(age: int,
                first_block: int,
                second_block: int,
                block_size: int
                ) -> int:
    if age <= 0:
        return 0
    if 0 < age < first_block:
        return 0
    if first_block <= age < first_block + second_block:
        return 1
    if (first_block + second_block <= age < first_block
            + second_block + block_size):
        return 2
    if age >= first_block + second_block + block_size:
        extra = (age - (first_block + second_block)) // block_size
        return 2 + extra