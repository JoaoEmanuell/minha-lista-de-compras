const resolve = require('path').resolve

const app_name = 'minha-lista-de-compras'
const path_to_static = resolve(__dirname, app_name, 'mlc', 'static')
const path_to_ts_compile_js = resolve(__dirname, app_name, 'ts_compile_js')

module.exports = {
    entry: {
        list: resolve(path_to_ts_compile_js, 'list.js'),
        login: resolve(path_to_ts_compile_js, 'login.js')
    },
    output: {
        filename: '[name]_index.js',
        path: path_to_static
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /none_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                        plugins: ['@babel/plugin-transform-runtime']
                    }
                }
            },
            {
                exclude: /none_modules/,
                test: /\.css$/i,
                use: ['style-loader', 'css-loader']
            }
        ]
    }
};