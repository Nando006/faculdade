<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $data = User::all(); // lista todos

        return [
            'status' => 200,
            'message' => 'Usuários listados com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $data = User::create($request->all()); // Cria um usuário

        return [
            'status' => 200,
            'message' => 'Usuário criado com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $data = User::findOrFail($id); // Procurando o usuário

        return [
            'status' => 200,
            'message' => 'Usuário Encontrado!',
            'data' => $data
        ];
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        $user = User::findOrFail($id);
        $user->update($request->all());

        return [
            'status' => 200,
            'message' => 'Usuário atualizado com sucesso!',
            'data' => $user
        ];
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        $user = User::findOrFail($id);
        $user->delete();

        return [
            'status' => 200,
            'message' => 'Usuário deletado com sucesso!',
            'data' => $user
        ];
    }
}
