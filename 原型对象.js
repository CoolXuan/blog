// 都是属性使用前加"."
// prototype  函数对象才有，（构造）函数原型对象
// __proto__  所有对象都有这属性，总是指向对应的（构造）函数的原型对象  /  prototype
// constructor :__proto__下面的constructor指向构造函数自己

// 引用类型：Object，Function ……就是对象

// 对象访问属性的时候，在自身属性查找，找不到再去__proto__原型链上查找，知道找不到为止，找不到返回undefined

function add() {
    console.log("add");
}

let person = {   //=====>new Object({name:"cx"})  对象的构造函数是Object()（爷）
    //person.__proto__ === Object.prototype 儿   __proto__找爹；prototype找儿
    //person 孙
    name: "cx",
    favorites: {
        game: '王者荣耀',
        sport: '篮球'
    }
}
//所有函数的原型都是Object（对象），所有Object的原型是null。
console.log("person", person);
console.log("person.__proto__=== Object.prototype", person.__proto__ === Object.prototype);  //构造器函数
// console.log("add.",person.__proto__.__proto__);  //函数

console.log(person.name);
person.__proto__.__proto__.a=123 //person.__proto__==>Object().__proto__=null
console.log(person.__proto__.a);