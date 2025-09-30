<?php

namespace App\Http\Controllers;

use App\Models\Categoria;
use Illuminate\Http\Request;

class CategoriaController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $data = Categoria::all();

        return [
            'status' => 200,
            'message' => 'Categorias listada com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $data = Categoria::create($request->all());

        return [
            'status' => 200,
            'message' => 'Categoria criada com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Display the specified resource.
     */
    public function show(Categoria $categoria)
    {
        return [
            'status' => 200,
            'message' => 'Categoria encontrada com sucesso!',
            'data' => $categoria
        ];
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Categoria $categoria)
    {
        return [
            'status' => 200,
            'message' => 'Categoria atualizada com sucesso!',
            'data' => $categoria->update($request->all()),
        ];
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Categoria $categoria)
    {
        return [
            'status' => 200,
            'message' => 'Categoria deletada com sucesso!',
            'data' => $categoria->delete(),
        ];
    }
}
