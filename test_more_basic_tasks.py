import pytest
from problems.more_basic_tasks import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12,
    task_13, task_14, task_15, task_16, task_17, task_18, task_19, task_20,
    task_21, task_22, task_23, task_24,
    task_25, task_26, task_27, task_28, task_29, task_30, task_31, task_32,
    task_33, task_34, task_35, task_36,
    task_37, task_38, task_39, task_40, task_41, task_42, task_43, task_44,
    task_45, task_46, task_47, task_48, task_49,
    task_50, task_51, task_52, task_53, task_54, task_55, task_56, task_57,
    task_58, task_59, task_60, task_61,
    task_62, task_63, task_64, task_65, task_66, task_67, task_68, task_69,
    task_70, task_71, task_72, task_73,
    task_74, task_75, task_76, task_77, task_78, task_79, task_80, task_81,
    task_82, task_83, task_84, task_85,
    task_86, task_87, task_88, task_89, task_90, task_91, task_92, task_93,
    task_94, task_95, task_96, task_97, task_98, task_99,
)


# ── LIST TESTS ────────────────────────────────────────────────────────────────

def test_task_0():
    assert task_0([1, 2, 3], 4) == [1, 2, 3, 4]
    assert task_0([], 7) == [7]
    assert task_0([0], 0) == [0, 0]


def test_task_1():
    assert task_1([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert task_1([4, 4, 4]) == [4]
    assert task_1([1, 2, 3]) == [1, 2, 3]
    assert task_1([]) == []


def test_task_2():
    assert task_2([3, 1, 4, 1, 5, 9, 2, 6]) == 6
    assert task_2([10, 20]) == 10
    assert task_2([5, 5, 3]) == 3


def test_task_3():
    assert task_3([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert task_3([[1], [2], [3]]) == [1, 2, 3]
    assert task_3([[]]) == []


def test_task_4():
    assert task_4([10, 20, 30, 40, 50]) == [10, 30, 50]
    assert task_4([1, 2]) == [1]
    assert task_4([7]) == [7]


def test_task_5():
    assert task_5([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert task_5([1, 2, 3], 0) == [1, 2, 3]
    assert task_5([1, 2, 3], 3) == [1, 2, 3]


def test_task_6():
    assert task_6([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert task_6([1, 2], [3, 4]) == []
    assert task_6([1, 1, 2], [1, 2, 2]) == [1, 2]


def test_task_7():
    assert task_7([1, 2, 3]) == [3, 2, 1]
    assert task_7([]) == []
    assert task_7([42]) == [42]


def test_task_8():
    assert task_8([1, 2, 2, 3], 2) == 2
    assert task_8(["a", "b", "a"], "a") == 2
    assert task_8([1, 2, 3], 9) == 0


def test_task_9():
    assert task_9([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert task_9([0, 5]) == [0, 25]
    assert task_9([]) == []


def test_task_10():
    assert task_10([1, 2, 3, 2, 1], 2) == [1, 3, 1]
    assert task_10([1, 1, 1], 1) == []
    assert task_10([1, 2, 3], 9) == [1, 2, 3]


def test_task_11():
    assert task_11([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert task_11([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert task_11([], 3) == []


def test_task_12():
    assert task_12([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert task_12([5]) == [5]
    assert task_12([1, -1, 1]) == [1, 0, 1]


# ── SET TESTS ─────────────────────────────────────────────────────────────────

def test_task_13():
    assert task_13({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
    assert task_13(set(), {1}) == {1}


def test_task_14():
    assert task_14({1, 2, 3}, {2, 3, 4}) == {2, 3}
    assert task_14({1, 2}, {3, 4}) == set()


def test_task_15():
    assert task_15({1, 2, 3}, {2, 3}) == {1}
    assert task_15({1, 2}, {1, 2, 3}) == set()


def test_task_16():
    assert task_16({1, 2, 3}, {3, 4, 5}) == {1, 2, 4, 5}
    assert task_16({1, 2}, {1, 2}) == set()


def test_task_17():
    assert task_17({1, 2}, {1, 2, 3}) is True
    assert task_17({1, 2, 3}, {1, 2}) is False
    assert task_17(set(), {1, 2}) is True


def test_task_18():
    assert task_18([3, 1, 2, 1, 3]) == [1, 2, 3]
    assert task_18([5, 5, 5]) == [5]
    assert task_18([]) == []


def test_task_19():
    assert task_19({1, 2}, {3, 4}) is True
    assert task_19({1, 2}, {2, 3}) is False


def test_task_20():
    result = task_20({1, 2})
    assert len(result) == 4
    assert set() in result
    assert {1} in result
    assert {2} in result
    assert {1, 2} in result


def test_task_21():
    assert task_21({1, 2}, [3, 4]) == {1, 2, 3, 4}
    assert task_21({1}, [1, 2]) == {1, 2}


def test_task_22():
    assert task_22("hello") == 4
    assert task_22("aaa") == 1
    assert task_22("") == 0


def test_task_23():
    assert task_23([1, 2, 2, 3, 3, 3]) == [2, 3]
    assert task_23([1, 2, 3]) == []
    assert task_23([4, 4]) == [4]


def test_task_24():
    assert task_24({3, 1, 4, 1, 5, 9}) == 9
    assert task_24({7}) == 7
    assert task_24({-1, -5, -2}) == -1


# ── TUPLE TESTS ───────────────────────────────────────────────────────────────

def test_task_25():
    assert task_25([3, 1, 4, 1, 5]) == (1, 5)
    assert task_25([7]) == (7, 7)
    assert task_25([-3, -1, -2]) == (-3, -1)


def test_task_26():
    assert task_26((1, 2, 3)) == 6
    assert task_26((0, 0, 0)) == 0
    assert task_26((-1, 4, 5)) == 8


def test_task_27():
    assert task_27(3, 7) == (7, 3)
    assert task_27(0, 0) == (0, 0)
    assert task_27(1, 2) == (2, 1)


def test_task_28():
    assert task_28([1, 2, 3]) == (1, 2, 3)
    assert task_28([]) == ()
    assert isinstance(task_28([1]), tuple)


def test_task_29():
    assert task_29((10, 20, 30), 20) == 1
    assert task_29((1, 2, 1), 1) == 0
    assert task_29((1, 2, 3), 9) == -1


def test_task_30():
    assert task_30((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert task_30((), (1,)) == (1,)
    assert task_30((1,), ()) == (1,)


def test_task_31():
    assert task_31(4) == (1, 4, 9, 16)
    assert task_31(1) == (1,)
    assert task_31(0) == ()


def test_task_32():
    assert task_32((1, 2, 3), 1, 99) == (1, 99, 3)
    assert task_32((10, 20, 30), 0, 5) == (5, 20, 30)


def test_task_33():
    assert task_33((1, 2, 2, 3), 2) == 2
    assert task_33((1, 2, 3), 9) == 0
    assert task_33(("a", "a", "b"), "a") == 2


def test_task_34():
    assert task_34([1, 2], ["a", "b"]) == [(1, "a"), (2, "b")]
    assert task_34([], []) == []
    assert task_34([1], [2]) == [(1, 2)]


def test_task_35():
    assert task_35((3, 1, 2)) == (1, 2, 3)
    assert task_35((5,)) == (5,)
    assert task_35(()) == ()


def test_task_36():
    assert task_36([("Alice", 85), ("Bob", 92), ("Carol", 78)]) == [
        ("Bob", 92), ("Alice", 85), ("Carol", 78)
    ]
    assert task_36([("x", 1)]) == [("x", 1)]


# ── DICT TESTS ────────────────────────────────────────────────────────────────

def test_task_37():
    assert task_37({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert task_37({"a": 1}, {"a": 2}) == {"a": 2}
    assert task_37({}, {"x": 10}) == {"x": 10}


def test_task_38():
    assert task_38({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert task_38({}) == {}


def test_task_39():
    result = task_39({"b": 3, "a": 1, "c": 2})
    assert list(result.values()) == [1, 2, 3]
    assert list(result.keys()) == ["a", "c", "b"]


def test_task_40():
    assert task_40(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}
    assert task_40([]) == {}
    assert task_40(["x"]) == {"x": 1}


def test_task_41():
    assert task_41({"a": 5, "b": 10, "c": 3}, 4) == ["a", "b"]
    assert task_41({"a": 1}, 5) == []
    assert task_41({"a": 5, "b": 5}, 4) == ["a", "b"]


def test_task_42():
    d = {"a": 1, "b": 2}
    result = task_42(d, "a")
    assert "a" not in result
    assert task_42({"x": 1}, "z") == {"x": 1}


def test_task_43():
    assert task_43({"a": {"b": {"c": 42}}}, ["a", "b", "c"]) == 42
    assert task_43({"a": 1}, ["a"]) == 1
    assert task_43({"a": 1}, ["b"]) is None
    assert task_43({"a": {"b": 1}}, ["a", "z"]) is None


def test_task_44():
    assert task_44({"foo_a": 1, "foo_b": 2, "bar_c": 3}, "foo") == {"foo_a": 1, "foo_b": 2}
    assert task_44({"abc": 1}, "xyz") == {}


def test_task_45():
    records = [{"type": "a", "v": 1}, {"type": "b", "v": 2}, {"type": "a", "v": 3}]
    result = task_45(records, "type")
    assert len(result["a"]) == 2
    assert len(result["b"]) == 1


def test_task_46():
    assert task_46({"a": 1, "b": 3, "c": 2}) == "b"
    assert task_46({"x": 10}) == "x"


def test_task_47():
    assert task_47({"a": 1, "b": 2}) == {"a": 2, "b": 4}
    assert task_47({}) == {}


def test_task_48():
    assert task_48(3) == {1: 1, 2: 4, 3: 9}
    assert task_48(1) == {1: 1}
    assert task_48(0) == {}


def test_task_49():
    assert task_49({"a": 1, "b": 2}, {"a": 10, "b": 20}) is True
    assert task_49({"a": 1}, {"b": 1}) is False
    assert task_49({}, {}) is True


# ── IF-ELSE TESTS ─────────────────────────────────────────────────────────────

def test_task_50():
    assert task_50(5) == "positive"
    assert task_50(-3) == "negative"
    assert task_50(0) == "zero"


def test_task_51():
    assert task_51(95) == "A"
    assert task_51(85) == "B"
    assert task_51(75) == "C"
    assert task_51(65) == "D"
    assert task_51(50) == "F"


def test_task_52():
    assert task_52(2000) is True
    assert task_52(1900) is False
    assert task_52(2024) is True
    assert task_52(2023) is False
    assert task_52(1600) is True


def test_task_53():
    assert task_53(-5) == 5
    assert task_53(5) == 5
    assert task_53(0) == 0


def test_task_54():
    assert task_54(4) == "even"
    assert task_54(7) == "odd"
    assert task_54(0) == "even"


def test_task_55():
    assert task_55(10) == 1
    assert task_55(-3) == -1
    assert task_55(0) == 0


def test_task_56():
    assert task_56(17.0) == "Underweight"
    assert task_56(22.0) == "Normal"
    assert task_56(27.0) == "Overweight"
    assert task_56(35.0) == "Obese"
    assert task_56(18.5) == "Normal"
    assert task_56(25.0) == "Overweight"


def test_task_57():
    assert task_57(3, 3, 3) == "equilateral"
    assert task_57(3, 3, 4) == "isosceles"
    assert task_57(3, 4, 5) == "scalene"


def test_task_58():
    assert task_58(15) == "fizzbuzz"
    assert task_58(9) == "fizz"
    assert task_58(10) == "buzz"
    assert task_58(7) == "7"


def test_task_59():
    assert task_59(1, 2, 3) == 3
    assert task_59(9, 5, 7) == 9
    assert task_59(4, 4, 4) == 4


def test_task_60():
    assert task_60(5, 1, 10) is True
    assert task_60(0, 1, 10) is False
    assert task_60(1, 1, 10) is True
    assert task_60(10, 1, 10) is True


def test_task_61():
    assert task_61(1) == "Winter"
    assert task_61(4) == "Spring"
    assert task_61(7) == "Summer"
    assert task_61(10) == "Autumn"
    assert task_61(12) == "Winter"
    assert task_61(3) == "Spring"


# ── FOR LOOP TESTS ────────────────────────────────────────────────────────────

def test_task_62():
    assert task_62([1, 2, 3, 4]) == 10
    assert task_62([]) == 0
    assert task_62([-1, 1]) == 0


def test_task_63():
    assert task_63(0) == 1
    assert task_63(1) == 1
    assert task_63(5) == 120
    assert task_63(6) == 720


def test_task_64():
    assert task_64(6) == [0, 1, 1, 2, 3, 5]
    assert task_64(1) == [0]
    assert task_64(0) == []


def test_task_65():
    assert task_65("racecar") is True
    assert task_65("hello") is False
    assert task_65("a") is True
    assert task_65("") is True


def test_task_66():
    assert task_66("Hello World") == 3
    assert task_66("bcdfg") == 0
    assert task_66("AEIOU") == 5


def test_task_67():
    assert task_67(10) == [2, 3, 5, 7]
    assert task_67(1) == []
    assert task_67(2) == [2]


def test_task_68():
    assert task_68([1, 2, 3, 4]) == 24
    assert task_68([]) == 1
    assert task_68([5]) == 5


def test_task_69():
    assert task_69("abca") == {"a": 3, "b": 1, "c": 2}
    assert task_69("") == {}
    assert task_69("xx") == {"x": 1}


def test_task_70():
    assert task_70(123) == 6
    assert task_70(0) == 0
    assert task_70(999) == 27


def test_task_71():
    result = task_71(500)
    assert 1 in result
    assert 153 in result
    assert 370 in result
    assert 371 in result
    assert 407 in result
    assert 4 not in result


def test_task_72():
    assert task_72([5, 3, 2]) == [0, 3, 4]
    assert task_72([]) == []
    assert task_72([10, 10]) == [0, 10]


def test_task_73():
    assert task_73([10, 20, 30]) == [(10, 0), (20, 1), (30, 2)]
    assert task_73([]) == []
    assert task_73([7]) == [(7, 0)]


# ── WHILE LOOP TESTS ──────────────────────────────────────────────────────────

def test_task_74():
    assert task_74(0) == 1
    assert task_74(9) == 1
    assert task_74(123) == 3
    assert task_74(1000) == 4


def test_task_75():
    assert task_75(1234) == 4321
    assert task_75(100) == 1
    assert task_75(0) == 0
    assert task_75(5) == 5


def test_task_76():
    assert task_76(493) == 7
    assert task_76(9) == 9
    assert task_76(38) == 2
    assert task_76(1) == 1


def test_task_77():
    assert task_77(48, 18) == 6
    assert task_77(7, 5) == 1
    assert task_77(100, 25) == 25


def test_task_78():
    assert task_78(1) is True
    assert task_78(2) is True
    assert task_78(8) is True
    assert task_78(6) is False
    assert task_78(16) is True


def test_task_79():
    assert task_79(8) == 3
    assert task_79(1) == 0
    assert task_79(4) == 2


def test_task_80():
    assert task_80(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert task_80(1) == [1]


def test_task_81():
    assert task_81(16) == 4
    assert task_81(17) == 4
    assert task_81(9) == 3
    assert task_81(0) == 0
    assert task_81(1) == 1


def test_task_82():
    assert task_82(4) == [1, 4, 9, 16]
    assert task_82(1) == [1]
    assert task_82(0) == []


def test_task_83():
    assert task_83(4) == [4, 3, 2, 1, 0]
    assert task_83(0) == [0]


def test_task_84():
    assert task_84(6) == 8
    assert task_84(1) == 0
    assert task_84(4) == 2


def test_task_85():
    assert task_85(9) == 2
    assert task_85(1) == 0
    assert task_85(27) == 3


# ── DATA TYPE TESTS ───────────────────────────────────────────────────────────

def test_task_86():
    assert task_86(3.9) == 3
    assert task_86(3.0) == 3
    assert task_86(0.5) == 0


def test_task_87():
    assert task_87(3.14159, 2) == 3.14
    assert task_87(2.5, 0) == 2.0 or task_87(2.5, 0) == 2
    assert task_87(1.005, 2) == round(1.005, 2)


def test_task_88():
    assert task_88("123") is True
    assert task_88("-45") is True
    assert task_88("12.3") is False
    assert task_88("abc") is False
    assert task_88("") is False


def test_task_89():
    assert task_89("3.14") is True
    assert task_89("42") is True
    assert task_89("abc") is False
    assert task_89("") is False


def test_task_90():
    assert task_90(10) == "1010"
    assert task_90(0) == "0"
    assert task_90(255) == "11111111"


def test_task_91():
    assert task_91(255) == "ff"
    assert task_91(16) == "10"
    assert task_91(0) == "0"


def test_task_92():
    assert task_92("A") == 65
    assert task_92("a") == 97
    assert task_92(" ") == 32


def test_task_93():
    assert task_93(65) == "A"
    assert task_93(97) == "a"
    assert task_93(32) == " "


def test_task_94():
    assert task_94("ab", 3) == "ababab"
    assert task_94("x", 1) == "x"
    assert task_94("hi", 0) == ""


def test_task_95():
    assert task_95("hello world") == "Hello World"
    assert task_95("python is fun") == "Python Is Fun"
    assert task_95("a") == "A"


def test_task_96():
    assert task_96("12345") is True
    assert task_96("123a5") is False
    assert task_96("") is True
    assert task_96("0") is True


def test_task_97():
    assert task_97("Hello World") == "Hll Wrld"
    assert task_97("aeiou") == ""
    assert task_97("bcdfg") == "bcdfg"


def test_task_98():
    assert task_98(3.14159) == "3.14"
    assert task_98(5.0) == "5.00"
    assert task_98(0.1) == "0.10"


def test_task_99():
    assert task_99(0) is True
    assert task_99(1) is True
    assert task_99(4) is True
    assert task_99(9) is True
    assert task_99(8) is False
    assert task_99(2) is False
