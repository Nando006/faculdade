<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    public function index(){
        return [
            'status' => 200,
            'message' => "Usuários listados com sucesso!",
            'users' => User::all()
        ];
    }

    public function store(Request $request) {
        $data = $request->all();
        $user = User::create($data);

        return [
            'status' => 200,
            'message' => "Usuário cadastrado com sucesso!",
            'user'=> $user
        ];
    }

    public function update(Request $request, $id) {
        $user = User::findOrFail($id);

        if(!$user) {
            return [
                'status' => 401,
                'message' => 'Usuário não foi encontrado'
            ];
        }

        $data = $request->only(['name', 'email']);

        if($request->filled('password')) {
            $data['password'] = bcrypt($data['password']);
        }

        $user->update($data);

        return [
            'status' => 200,
            'message' => "Usuário atualizado com sucesso!",
            'user' => $user
        ];
    }

    public function destroy($id) {
        $user = User::findOrFail($id);
        $user->delete();

        return [
            'status' => 200,
            'message' => "Usuário deletado com sucesso!"
        ];
    }
}
