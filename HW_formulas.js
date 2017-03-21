
    
/* 1 Написать функцию для определения НОК для двух чисел */
function f_lcm(f_lcm1, f_lcm2){
    var max_f_lcm = Math.max(f_lcm1, f_lcm2)
    while(true){
            if(max_f_lcm % f_lcm1 === 0 && max_f_lcm % f_lcm2 === 0){
                f_lcm = max_f_lcm
                break
            }
            else{
                max_f_lcm +=1
            }
        }
    return f_lcm
}
    
f_lcm(3,5)

/* 2 Написать функцию, которая принимает список, и возвращает словарь в формате: "тип данных: количество объектов" */


function list_to_dict(arr){
    var dict = {}
    arr.forEach(function(item, i, arr){
        if (!(typeof(item) in dict)) {
            dict[typeof(item)] = arr.filter(function(type) {
                return typeof(type) === typeof(item);
            }).length;
        }});
    return dict;
}

list_to_dict([1, 2, 'a', 3])

/* 3 Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей */

var dict1 = {1:'a', 2:'b', 3:'c'}
var dict2 = {3:'d', 4:'e', 5:'f'}

function dict_comp(dict_1, dict_2){
    var num_of_shk = 0
    var dict1_keys = Object.keys(dict_1)
    dict1_keys.forEach(function(item, i, dict1_keys){
        if(item in dict_2){
            num_of_shk++
        }
    });
    return num_of_shk;
}

dict_comp(dict1, dict2)

/* 4 Написать функцию, которая принимает любое количество аргументов, она должна вернуть список типов, принятых аргументов */


function f_any_arg() {
    var l = [];
    for (var i = 0; i < arguments.length; i++){
        l.push(typeof(arguments[i]))
        }
    return l
}

f_any_arg(3, 'a')



/* 5 Написать функцию, которая принимает на вход список списков (матрицу) и выводит ее в виде матрицы (один ряд на одной строке) в консоль */

var l = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

function f_matrix(l0){
    console.log(l[0])
    console.log(l[1])
    console.log(l[2])
}
f_matrix(l)

/* 6 Написать функцию, которая принимает любое количество аргументов - списков, 
она должна возвращать список из всех объектов списков, но каждый объект должен быть уникальным */
array1 = [1, 2, 3]
array2 = [2, 'a', 6]

function f_join_list(){
    Array.prototype.unique = function() {
    var a = this.concat();
    for(var i = 0; i < a.length; ++i) {
        for(var j = i + 1; j < a.length; ++j) {
            if(a[i] === a[j])
                a.splice(j--, 1);
        }
    }
    return a;
};
var join_l = array1.concat(array2).unique(); 
    return join_l
}

f_join_list(array1, array2)

